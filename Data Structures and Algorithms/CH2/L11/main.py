def num_possible_orders(num_posts):
    product = 1
    while num_posts > 1:
        product *= num_posts
        num_posts -= 1
    return product
