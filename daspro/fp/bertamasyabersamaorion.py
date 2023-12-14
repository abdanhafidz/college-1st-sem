N = int(input())
price_best = None
quality_best = None

for _ in range(N):
    item_info = input().split()
    item_id, item_name, item_price, item_quality = int(item_info[0]), item_info[1], int(item_info[2]), int(item_info[3])

    
    if price_best is None or item_price < price_best[2] or (item_price == price_best[2] and item_id < price_best[0]):
        price_best = (item_id, item_name, item_price, item_quality)

    
    if quality_best is None or item_quality > quality_best[3] or (item_quality == quality_best[3] and item_id < quality_best[0]):
        quality_best = (item_id, item_name, item_price, item_quality)


print(f"Best item for price is: {price_best[0]} {price_best[1]} {price_best[2]} {price_best[3]}")
print(f"Best item for quality is : {quality_best[0]} {quality_best[1]} {quality_best[2]} {quality_best[3]}")