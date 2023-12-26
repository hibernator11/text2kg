from KG import KG
import pickle
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
#from textwrap import wrap
from nltk.tokenize import sent_tokenize
import sys

# python3 mrebel-en-32-huggingface.py wikipedia cervantes-en
# python3 mrebel-en-32-huggingface.py nls-text-indiaPapers 74463059

def extract_triplets_typed(text):
    triplets = []
    relation = ''
    text = text.strip()
    current = 'x'
    subject, relation, object_, object_type, subject_type = '','','','',''

    for token in text.replace("<s>", "").replace("<pad>", "").replace("</s>", "").replace("tp_XX", "").replace("__en__", "").split():
        if token == "<triplet>" or token == "<relation>":
            current = 't'
            if relation != '':
                triplets.append({'head': subject.strip(), 'head_type': subject_type, 'type': relation.strip(),'tail': object_.strip(), 'tail_type': object_type})
                relation = ''
            subject = ''
        elif token.startswith("<") and token.endswith(">"):
            if current == 't' or current == 'o':
                current = 's'
                if relation != '':
                    triplets.append({'head': subject.strip(), 'head_type': subject_type, 'type': relation.strip(),'tail': object_.strip(), 'tail_type': object_type})
                object_ = ''
                subject_type = token[1:-1]
            else:
                current = 'o'
                object_type = token[1:-1]
                relation = ''
        else:
            if current == 't':
                subject += ' ' + token
            elif current == 's':
                object_ += ' ' + token
            elif current == 'o':
                relation += ' ' + token
    if subject != '' and relation != '' and object_ != '' and object_type != '' and subject_type != '':
        triplets.append({'head': subject.strip(), 'head_type': subject_type, 'type': relation.strip(),'tail': object_.strip(), 'tail_type': object_type})
    return triplets

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("Babelscape/mrebel-large-32", src_lang="en_XX", tgt_lang="tp_XX") 
# Here we set English ("en_XX") as source language. To change the source language swap the first token of the input for your desired language or change to supported language. For catalan ("ca_XX") or greek ("el_EL") (not included in mBART pretraining) you need a workaround:
# tokenizer._src_lang = "ca_XX"
# tokenizer.cur_lang_code_id = tokenizer.convert_tokens_to_ids("ca_XX")
# tokenizer.set_src_lang_special_tokens("ca_XX")
model = AutoModelForSeq2SeqLM.from_pretrained("Babelscape/mrebel-large-32")
gen_kwargs = {
    "max_length": 256,
    "length_penalty": 0,
    "num_beams": 3,
    "num_return_sequences": 3,
    "forced_bos_token_id": None,
}


# Text to extract triplets from
#text = 'The Red Hot Chili Peppers were formed in Los Angeles by Kiedis, Flea, guitarist Hillel Slovak and drummer Jack Irons.'

# create kg
kg = KG()
text = ''
input_folder = 'input/'

org_folder = sys.argv[1]

#org_folder = 'lc'
#org_folder = 'nls-text-indiaPapers'
#org_folder = 'wikipedia'

folder = input_folder + org_folder + '/'
#text_file = 'napoleon-en'
#text_file = 'cervantes-en'
#text_file = 'sn84020422-1962-04-19-ed-1-seq-4-ocr'
#text_file = '74463059'

text_file = sys.argv[2]

with open(folder+text_file+'.txt') as f:
    text = f.read()
    #print(wrap(text, 250))
    
    #for t in wrap(text, 250):
    for t in sent_tokenize(text):
        print(t) 
        # Tokenizer text
        model_inputs = tokenizer(t, max_length=256, padding=True, truncation=True, return_tensors = 'pt')

        # Generate
        generated_tokens = model.generate(
            model_inputs["input_ids"].to(model.device),
            attention_mask=model_inputs["attention_mask"].to(model.device),
            decoder_start_token_id = tokenizer.convert_tokens_to_ids("tp_XX"),
            **gen_kwargs,
        )

        #Extract text
        decoded_preds = tokenizer.batch_decode(generated_tokens, skip_special_tokens=False)

        # Extract triplets
        for idx, sentence in enumerate(decoded_preds):
            print(f'Prediction triplets sentence {idx}')
            #print(extract_triplets_typed(sentence))
            relations = extract_triplets_typed(sentence)
            for relation in relations:
                kg.add_relation(relation)

    with open('output/pickle/kb_rebel32_'+ org_folder + '_' + text_file+'.pickle', 'wb') as f:
        pickle.dump(kg, f)
    
   