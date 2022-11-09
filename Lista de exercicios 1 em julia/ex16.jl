print("você fuma há quantos anos?:\n")
anos = parse(Int64, readline())
print("você fuma quantos cigarros por dia:\n")
singaro = parse(Int64, readline())
carse = (anos * 365 * singaro) / 144
print("você perdeu $carse dias de vida\n")
print("singaro da carse")
