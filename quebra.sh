#!/usr/bin/env bash

echo "Testando chaves... "
keys="$(quebra-pf -d utils/clean_dict -t $1)"

echo "Chaves possíveis:$keys"

python utils/decifrador.py $1 $keys

echo "Arquivos criados"
