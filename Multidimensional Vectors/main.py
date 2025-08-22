from dimensional_vector import DimensionalVector
def main():
    # Create a 5D vector (all zeros initially)
    v =  DimensionalVector(5) 
    print("\nInitial vector v:", v)   # <0, 0, 0, 0, 0>

    # Set values
    v[1] = 23
    v[-1] = 45   # Python supports negative indexing
    print("After setting values v:", v)  # <0, 23, 0, 0, 45>

    # Create vector u
    u = DimensionalVector(5)
    print("\nInitial vector u:", u)   # <0, 0, 0, 0, 0>
    
    # Set values
    u[1] = 6
    u[2] = 2
    print("After setting values u:", u)   # <0, 6, 2, 0, 0>

    # Access values
    print("\nv[4] =", v[4])   # → 45
    print("u[1] =", u[1])   # → 6

    # Vector addition
    w = u + v
    print("\nVector Addition:")
    print("w = u + v=", w)  

    # Adding vector and list
    z = u + [5, 10, 3, -4, 1]
    print("\nAdding vector and list:")
    print("z = u + [5, 10, 3, -4, 1]=", z) # <5, 16, 5, -4, 1>

    # Equality check
    print("\nEquality Check:")
    print("u == v: ", u == v)   # False
    print("u != v: ", u != v)   # True

     # Iteration & len
    print("\nIteration & Length:")
    print("Length of v:", len(v))
    print("Sum of v:", sum(v)) 

    print("Length of u:", len(u))   # 5
    print("Sum of u:", sum(u))  


if __name__ == "__main__":
    main()