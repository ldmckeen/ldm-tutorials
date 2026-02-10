from enum import Enum, auto


class DiscountType(Enum):
    STANDARD = auto()
    SEASONAL = auto()
    WEIGHT = auto()


def get_discounted_price(cart_weight, total_price, discount_type):
    
    if discount_type == DiscountType.STANDARD:
        return total_price - (total_price * 0.06)
    elif discount_type == DiscountType.SEASONAL:
        return total_price - (total_price * 0.12)
    elif discount_type == DiscountType.WEIGHT:
        if cart_weight <= 10:
            return total_price - (total_price * 0.06)
        else:
            return total_price - (total_price * 0.18)
    
    
        
    
if __name__ == '__main__':
    print(get_discounted_price(12, 100, DiscountType.WEIGHT))









