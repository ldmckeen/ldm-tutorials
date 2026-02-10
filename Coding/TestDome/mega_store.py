"""
A Megastore offers three types of discounts, which are represented as DiscountType enum.

Implement the get_discounted_price function which would take the weight of the shopping cart,
the total price, and the discount type. It should return the final discounted price based on the
discount schemes as shown below.

Standard Discount:
    Weight any
    6%
    
Seasonal Discount:
    Weight any
    12%
    
Seasonal Discount:
    Weight <=10
    6%
    
    Weight > 10
    18%
    
    
"""

from enum import Enum, auto


class DiscountType(Enum):
    STANDARD = auto()
    SEASONAL = auto()
    WEIGHT = auto()


def get_discounted_price(cart_weight, total_price, discount_type):
    if discount_type is DiscountType.STANDARD:
        return total_price - (total_price * 0.06)
    elif discount_type is DiscountType.SEASONAL:
        return total_price - (total_price * 0.12)
    elif discount_type is DiscountType.WEIGHT:
        if cart_weight <= 10:
            # 6%
            return total_price - (total_price * 0.06)

        else:
            return total_price - (total_price * 0.18)


if __name__ == '__main__':
    
    print(get_discounted_price(12, 100, DiscountType.WEIGHT))

