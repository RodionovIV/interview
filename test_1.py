def process_orders(orders):
    completed_orders = filter(lambda order: order['status'] == 'complete', orders)

    sorted_orders = sorted(completed_orders, key=lambda x: x['total_price'], reverse=True)

    top_orders = sorted_orders[:3]

    order_ids = []
    for i in range(3):
        order_ids.append(top_orders[i]['id'])

    return order_ids

