####Converter cada linha de um JSONL com essa estrutura:
#{
#  "uid": "0000031909",
#  "title": "Girls Ballet Tutu Neon Pink",
#  "content": "High quality 3 layer ballet tutu. 12 inches in length",
#  "target_ind": [...],
 # "target_rel": [...]
#}
###Tranformar no formato ShareGPT
#{
#  "conversations": [
#    {"from": "human", "value": "Girls Ballet Tutu Neon Pink"},
#    {"from": "gpt", "value": "High quality 3 layer ballet tutu. 12 inches in length"},
#    {"from": "system", "value": "Product Description"}
#  ],
#  "source": "LF-Amazon-1.3M"
#}

import json

def converter_jsonl_para_conversations(input_file, output_file, source="LF-Amazon-1.3M"):
    """
    Converte arquivo JSONL no formato bruto para o formato de conversations + source.
    
    input_file: caminho do arquivo JSONL de entrada.
    output_file: caminho do arquivo JSONL convertido.
    source: valor fixo para o campo "source".
    """
    with open(input_file, 'r', encoding='utf-8') as infile:
        linhas = infile.readlines()
    
    resultado = []
    
    for linha in linhas:
        item = json.loads(linha)
        conversa = {
            "conversations": [
                {"from": "human", "value": item["title"]},
                {"from": "gpt", "value": item["content"]},
                {"from": "system", "value": "Product Description"}
            ],
            "source": source
        }
        resultado.append(conversa)
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(resultado, outfile, ensure_ascii=False, indent=2)

# Conversão
converter_jsonl_para_conversations(
    input_file='./TechChalengeFase3/trn.json',
    output_file='./TechChalengeFase3/TRN3.json'
)
