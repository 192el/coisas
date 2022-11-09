print("em que ano você nasceu?:\n")
nascimento = parse(Int64, readline())
idade = 2022 - nascimento
if idade >= 16 && idade < 18
    print("você pode votar!")
elseif idade >= 18
    print("você é obrigado a votar!")
else
    print("você não pode votar")
end
