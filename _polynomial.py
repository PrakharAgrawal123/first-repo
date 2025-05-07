class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None

def addPolynomials(poly1, poly2):
    head = None
    tail = None

    while poly1 and poly2:
        if poly1.power == poly2.power:
            new_coeff = poly1.coeff + poly2.coeff
            new_node = Node(new_coeff, poly1.power)

            if head is None:
                head = tail = new_node
            else:
                tail.next = new_node
                tail = new_node

            poly1 = poly1.next
            poly2 = poly2.next
        else:
            print("Powers are not matching!")
            return None
    return head

def printPolynomial(poly):
    while poly:
        print(f"{poly.coeff}x^{poly.power}", end=" ")
        if poly.next:
            print("+", end=" ")
        poly = poly.next
    print()

# Create first polynomial: 3x^2 + 2x^1 + 1x^0
poly1 = Node(3, 2)
poly1.next = Node(2, 1)
poly1.next.next = Node(1, 0)

# Create second polynomial: 5x^2 + 4x^1 + 6x^0
poly2 = Node(5, 2)
poly2.next = Node(4, 1)
poly2.next.next = Node(6, 0)

print("BEFORE ADDING POLYNOMIAL 1: ")
printPolynomial(poly1)

print("\nBEFORE ADDING POLYNOMIAL 2: ")
printPolynomial(poly2)



# Add the two polynomials
result = addPolynomials(poly1, poly2)

print("\nAfter Adding Sum of polynomials:")
printPolynomial(result)
