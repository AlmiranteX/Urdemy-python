lugares = ['israel', 'eua', 'suica', 'japao', 'hawai']

print(f"Lista nomal\n\t{lugares}")

print(f"Lista sorted ordem alfabetica temporariamente\n\t{sorted(lugares)}")

print(f"Lista sorted orden alfabetica alterada temporariamente\n\t{sorted(lugares, reverse=True)}")

print(f"Lista original\n\t{lugares}")

lugares.sort(reverse=True)
print(f"Lista alterada orden alfabetica\n\t{lugares}")
lugares.sort(reverse=False)
print(f"Lista novamente alterada\n\t{lugares}")

