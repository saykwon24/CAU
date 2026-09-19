import time
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# Global Configuration & Seed
# ==========================================
np.random.seed(42)

def print_header(title):
    print(f"\n{'='*50}\n{title}\n{'='*50}")



# ==========================================
# Section 1: Algorithm Analysis
# ==========================================

## 1.1. Moving Averages
def movingAverages1(X, n, k):
    """O(n*k) Slow version: Computes using the literal definition."""
    A = np.zeros(n)                       # create an empty(elements are all zero) array of size of n
    for i in range(k - 1, n):
        A[i] = np.sum(X[i - k + 1 : i + 1]) / k
    return A

def movingAverages2(X, n, k):
    """O(n) Optimized version: Computes using an intermediate sliding sum."""
    A = np.zeros(n)
    current_sum = np.sum(X[:k])           # X[0] + ... + X[k-1]
    A[k - 1] = current_sum / k
    for i in range(k, n):
        current_sum += X[i] - X[i - k]    # X[i-k+1] + ... + X[i] for i == i
        A[i] = current_sum / k
    return A

def run_moving_averages_experiments():
    print_header("1. Algorithm Analysis")
    print("    1. Algorithm Analysis: Moving Averages")
    
    ## 1.1.(a) Histogram of 1000 ratios for n=2^5, k=2^4
    n_a, k_a = 2**5, 2**4
    ratios_a = []
    for _ in range(1000):
        X = np.random.uniform(0, 1, n_a)
        
        # Execution time for movingAverages1
        t0 = time.perf_counter()
        movingAverages1(X, n_a, k_a)
        t1 = time.perf_counter()
        time1 = t1 - t0
        
        # Execution time for movingAverages2
        t0 = time.perf_counter()
        movingAverages2(X, n_a, k_a)
        t1 = time.perf_counter()
        time2 = t1 - t0
        
        # Protect against division by zero microsecond captures
        if time2 > 0:
            ratios_a.append(time1 / time2)
            
    plt.figure(figsize=(8, 5))
    plt.hist(ratios_a, bins=30, color='skyblue', edgecolor='black')
    plt.title("Execution Time Ratio (Slow / Optimized) - Moving Averages")
    plt.xlabel("Ratio (Time1 / Time2)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("./ratio_hist2.jpg")
    plt.close()
    print("        (a) Saved plot to ./ratio_hist2.jpg")

    ## 1.1.(b) Line plot for varying n with k=2^3
    k_b = 2**3
    n_values = [2**4, 2**5, 2**6, 2**7, 2**8]
    min_ratios, max_ratios, avg_ratios = [], [], []
    
    for n_b in n_values:
        curr_ratios = []
        for _ in range(100):  # Using 100 iterations per size for clean benchmarking
            X = np.random.uniform(0, 1, n_b)
            t0 = time.perf_counter()
            movingAverages1(X, n_b, k_b)
            time1 = time.perf_counter() - t0
            
            t0 = time.perf_counter()
            movingAverages2(X, n_b, k_b)
            time2 = time.perf_counter() - t0
            
            if time2 > 0:
                curr_ratios.append(time1 / time2)
        min_ratios.append(np.min(curr_ratios))
        max_ratios.append(np.max(curr_ratios))
        avg_ratios.append(np.mean(curr_ratios))

    plt.figure(figsize=(8, 5))
    plt.plot(n_values, min_ratios, label='Min Ratio', marker='o')
    plt.plot(n_values, max_ratios, label='Max Ratio', marker='s')
    plt.plot(n_values, avg_ratios, label='Avg Ratio', marker='^')
    plt.title("Execution Time Ratios vs Input Size n (k=8)")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Execution Time Ratio")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("./ratio_plot2.jpg")
    plt.close()
    print("        (b) Saved plot to ./ratio_plot2.jpg\n")


## 1.2 Count Ones in O(n)
def countOnesButSlow(A, n):
    """O(n^2) benchmark version."""
    c = 0    # counter
    for i in range(n):
        j = 0
        while j < n and A[i, j] == 1:
            c += 1
            j += 1
    return c

def countOnes(A, n):
    """
    O(n) version.
    Since 1s precede 0s and row i has >= 1s than row i+1,
    we trace the staircase boundary starting from top-right.
    """
    total_ones = 0
    col = n - 1
    for row in range(n):
        while col >= 0 and A[row, col] == 0:
            col -= 1
        # If col drops below 0, no remaining rows have 1s
        if col < 0:
            break
        total_ones += (col + 1)
    return total_ones

def generate_staircase_matrix(n):
    """Generates a valid binary matrix fulfilling the assignment's row constraints."""
    A = np.zeros((n, n), dtype=int)
    # Start with a random count for row 0, then strictly non-increasing downwards
    prev_ones = np.random.randint(0, n + 1)
    for i in range(n):
        ones_count = np.random.randint(0, prev_ones + 1) if prev_ones > 0 else 0
        A[i, :ones_count] = 1
        prev_ones = ones_count
    return A

def run_count_ones_experiments():
    print("    2. Algorithm Analysis: Count Ones")
    
    ## 1.2.(a) Histogram for n=2^6
    n = 2**6
    ratios = []
    for _ in range(1000):
        A = generate_staircase_matrix(n)
        
        t0 = time.perf_counter()
        countOnesButSlow(A, n)
        t1 = time.perf_counter()
        t_slow = t1 - t0
        
        t0 = time.perf_counter()
        countOnes(A, n)
        t1 = time.perf_counter()
        t_fast = t1 - t0
        
        if t_fast > 0:
            ratios.append(t_slow / t_fast)
            
    plt.figure(figsize=(8, 5))
    plt.hist(ratios, bins=30, color='lightgreen', edgecolor='black')
    plt.title("Execution Time Ratio (Slow / O(n)) - Count Ones")
    plt.xlabel("Ratio (t_slow / t_fast)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("./ratio_hist4.jpg")
    plt.close()
    print("        (a) Saved plot to ./ratio_hist4.jpg")

    ## 1.2.(b) Line plot for n = 2^4 to 2^8
    n_values = [2**4, 2**5, 2**6, 2**7, 2**8]
    min_r, max_r, avg_r = [], [], []
    for n_val in n_values:
        curr_ratios = []
        for _ in range(100):
            A = generate_staircase_matrix(n_val)
            t0 = time.perf_counter()
            countOnesButSlow(A, n_val)
            ts = time.perf_counter() - t0
            
            t0 = time.perf_counter()
            countOnes(A, n_val)
            tf = time.perf_counter() - t0
            
            if tf > 0:
                curr_ratios.append(ts / tf)
        min_r.append(np.min(curr_ratios))
        max_r.append(np.max(curr_ratios))
        avg_r.append(np.mean(curr_ratios))

    plt.figure(figsize=(8, 5))
    plt.plot(n_values, min_r, label='Min Ratio', marker='o')
    plt.plot(n_values, max_r, label='Max Ratio', marker='s')
    plt.plot(n_values, avg_r, label='Avg Ratio', marker='^')
    plt.title("Count Ones Execution Time Ratio vs Input Size n")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Ratio")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("./ratio_plot4.jpg")
    plt.close()
    print("        (b) Saved plot to ./ratio_plot4.jpg\n")



# ==========================================
# Section 2: Recursion
# ==========================================

def gcd1(a, b):
    """Recursive GCD using modulo arithmetic."""
    print(f"        computing gcd1({a}, {b})")
    if b == 0:
        return a
    return gcd1(b, a % b)

def gcd2(a, b):
    """Recursive GCD using subtraction."""
    print(f"        computing gcd2({a}, {b})")
    if a == b:
        return a
    if a > b:
        return gcd2(a - b, b)
    else:
        return gcd2(a, b - a)

def divide(a, b):
    """Recursive division returning (quotient, remainder) using only +/-."""
    print(f"        computing divide({a}, {b})")
    if a < b:
        return (0, a)
    q, r = divide(a - b, b)
    return (q + 1, r)

def run_recursion_section():
    print_header("2. Recursion")
    
    ## 2.1.(a)
    print("    1.(a) GCD1 & GCD2 Test: a=493, b=33")
    res1 = gcd1(493, 33)
    print(f"        gcd1(493, 33) is {res1}\n")
    res2 = gcd2(493, 33)
    print(f"        gcd2(493, 33) is {res2}")

    ## 2.1.(b)
    print("\n    1.(b) GCD1 & GCD2 Test: a=225, b=13")
    res1 = gcd1(225, 13)
    print(f"        gcd1(225, 13) is {res1}\n")
    res2 = gcd2(225, 13)
    print(f"        gcd2(225, 13) is {res2}")

    ## 2.2.(a)
    print("\n    2.(a) Divide Test: a=413, b=31")
    q, r = divide(413, 31)
    print(f"        divide(413, 31) is quotient: {q}, remainder: {r}")

    ## 2.2.(b)
    print("\n    2.(b) Divide Test: a=325, b=113")
    q, r = divide(325, 113)
    print(f"        divide(325, 113) is quotient: {q}, remainder: {r}")



# ==========================================
# Section 3: Basic Data Structure
# ==========================================

def run_sparse_matrix_experiments():
    print()    # new line
    print_header("3. Basic Data Structure: Sparse Matrix Offsets")
    # Note: In standard row-major indexing, flat offset = row * cols + col.
    # Total offset of dense matrix cells = sum of flat indices of nonzero values.
    # Total offset of coordinate array = sum of flat indices within the coordinate array itself.
    
    def process_sparse_offsets(num_matrices, min_ones, max_ones, save_name):
        offset_ratios = []
        # Simulate matrices efficiently to avoid memory overflow of 10^6 objects
        for _ in range(num_matrices):
            k = np.random.randint(min_ones, max_ones + 1)
            # Pick k distinct flat index locations in a 10x10 matrix
            flat_indices = np.random.choice(100, k, replace=False)
            
            # 1. Total offset of nonzero cells in A (sum of their flat linear coordinates)
            total_offset_A = np.sum(flat_indices)
            
            # 2. Coordinate list array has 2*k elements stored consecutively.
            # Sum of offsets inside the coordinate list = 0 + 1 + ... + (2k-1)
            total_offset_locs = (2*k - 1) * (2*k) // 2    # using // instead of / to keep the type 'int'
            
            if total_offset_locs > 0:
                offset_ratios.append(total_offset_A / total_offset_locs)
                
        plt.figure(figsize=(8, 5))
        plt.hist(offset_ratios, bins=40, color='salmon', edgecolor='black')
        plt.title(f"Ratio of Offsets (Dense Nonzeros / Sparse Coordinates) [{min_ones}-{max_ones} ones]")
        plt.xlabel("Offset Ratio")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig(save_name)
        plt.close()
        print(f"    Saved sparse matrix plot to {save_name}")

    process_sparse_offsets(10**6, 1, 5, "./sparse_hist1.jpg")
    process_sparse_offsets(10**6, 10, 20, "./sparse_hist2.jpg")



# ==========================================
# Section 4: Lists
# ==========================================

def run_list_vs_array_deletion():
    print()    # new line
    print_header("4. Lists")
    print("    1. Lists: Deletion Benchmarks")
    
    # Repeat deletion benchmarking
    t_list_del, t_array_del = [], []
    for _ in range(1000):
        # Python List Deletion
        lst = list(range(100))
        t0 = time.perf_counter()
        while lst:
            lst.pop(0)    # O(n) shift overhead per pop
        t_list_del.append(time.perf_counter() - t0)
        
        # Numpy Array Deletion
        arr = np.arange(100)
        t0 = time.perf_counter()
        while arr.size > 0:
            arr = np.delete(arr, 0)    # Creates a deep copy overhead every cycle
        t_array_del.append(time.perf_counter() - t0)

    ## 4.1.(a)
    plt.figure(figsize=(8, 4))
    plt.hist(t_list_del, bins=30, color='gold', edgecolor='black')
    plt.title("Elapsed Time for Removing Elements from a Python List (n=100)")
    plt.xlabel("Time (seconds)")
    plt.savefig("./histListDel.jpg")
    plt.close()
    print("        (a) Saved plot to ./histListDel.jpg")


    ## 4.1.(b)
    plt.figure(figsize=(8, 4))
    plt.hist(t_array_del, bins=30, color='orange', edgecolor='black')
    plt.title("Elapsed Time for Removing Elements from a Numpy Array (n=100)")
    plt.xlabel("Time (seconds)")
    plt.savefig("./histArrayDel.jpg")
    plt.close()
    print("        (b) Saved plot to ./histArrayDel.jpg")


    ## 4.1.(c) Scaling behavior across n
    sizes = [100, 300, 500, 700, 900]
    min_rat, avg_rat, max_rat = [], [], []
    
    for n in sizes:
        ratios = []
        for _ in range(30):  # Reduced sample size per scaling test to keep script execution snappy
            lst = list(range(n))
            t0 = time.perf_counter()
            while lst: lst.pop(0)
            tl = time.perf_counter() - t0
            
            arr = np.arange(n)
            t0 = time.perf_counter()
            while arr.size > 0: arr = np.delete(arr, 0)
            ta = time.perf_counter() - t0
            
            if ta > 0: ratios.append(tl / ta)
            
        min_rat.append(np.min(ratios))
        avg_rat.append(np.mean(ratios))
        max_rat.append(np.max(ratios))

    plt.figure(figsize=(8, 5))
    plt.plot(sizes, min_rat, label='Min Ratio', marker='o')
    plt.plot(sizes, avg_rat, label='Avg Ratio', marker='^')
    plt.plot(sizes, max_rat, label='Max Ratio', marker='s')
    plt.title("Deletion Execution Ratio (List / Array) vs Size n")
    plt.xlabel("Size (n)")
    plt.ylabel("Ratio (Time_List / Time_Array)")
    plt.legend()
    plt.grid(True)
    plt.savefig("./ListVsArrayDel.jpg")
    plt.close()
    print("        (c) Saved plot to ./ListVsArrayDel.jpg")


## 4.2 Sharing Matrix Functions
def SharingList(A):
    """Converts sharing matrix A into a list of shared elements grouped by column index."""
    num_elements, num_groups = A.shape
    shared_representation = []
    for g in range(num_groups):
        # Collects indices of rows where group column is active (1)
        shared_representation.append([e for e in range(num_elements) if A[e, g] == 1])
    return shared_representation

def FindPopularList(shared_lists, num_elements=20):
    """Finds the most frequently shared element iterating through native Python lists."""
    counts = [0] * num_elements
    for group in shared_lists:
        for elem in group:
            counts[elem] += 1
    return counts.index(max(counts))

def FindPopularArray(A):
    """Finds the most shared element by leveraging pure vector operations."""
    # Summing horizontally calculates membership frequency per element instantly
    return int(np.argmax(np.sum(A, axis=1)))

def run_sharing_matrix():
    print()    # new line
    print("    2. Lists: Sharing Matrix")
    np.random.seed(0)
    # Generates binary matrix representing group memberships
    A = np.random.binomial(1, 0.2, size=(20, 10))
    
    ## 4.2.(a)
    s_list = SharingList(A)
    print("        (a) Result of SharingList(A):")
    print(f"            {s_list}")
    
    
    ## 4.2.(b)
    pop_list = FindPopularList(s_list, num_elements=20)
    pop_arr = FindPopularArray(A)
    print(f"        (b) Most popular element found via List: {pop_list}")
    print(f"            Most popular element found via Array: {pop_arr}")

    # Benchmark ratios
    ratios = []
    for _ in range(1000):
        t0 = time.perf_counter()
        FindPopularList(s_list, num_elements=20)
        tl = time.perf_counter() - t0
        
        t0 = time.perf_counter()
        FindPopularArray(A)
        ta = time.perf_counter() - t0
        
        if ta > 0: ratios.append(tl / ta)

    plt.figure(figsize=(8, 4))
    plt.hist(ratios, bins=30, color='purple', edgecolor='black')
    plt.title("Execution Ratio (FindPopularList / FindPopularArray)")
    plt.xlabel("Ratio")
    plt.savefig("./HistSharing.jpg")
    plt.close()
    print("            Saved plot to ./HistSharing.jpg")



# ==========================================
# Section 5: Sets
# ==========================================

class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class OrderedSetLL:
    """Linked List representation of an Ordered Set."""
    def __init__(self, elements):
        self.head = None
        # Sort beforehand to strictly preserve ordering principles
        for el in sorted(elements, reverse=True):
            new_node = Node(el)
            new_node.next = self.head
            self.head = new_node

    def member(self, e):
        """Standard Member evaluation matching Algorithm 5 logic."""
        p = self.head
        if p is None: return False
        while True:
            if p.elem < e:
                if p.next is None: return False
                p = p.next
            elif p.elem > e:
                return False
            else:
                return True

def Subset(setA_ll, setB_ll):
    """Standard Subset search matching Algorithm 6 logic."""
    p = setA_ll.head
    if p is None: return True
    while True:
        if setB_ll.member(p.elem):
            if p.next is None: return True
            p = p.next
        else:
            return False

def SubsetFast(setA_ll, setB_ll):
    """
    O(|A| + |B|) highly optimized Subset evaluation.
    Traverses both linked lists sequentially using simultaneous dual pointers.
    """
    ptrA = setA_ll.head
    ptrB = setB_ll.head
    
    while ptrA is not None:
        # Fast-forward Set B pointer until matching or exceeding current Set A target
        while ptrB is not None and ptrB.elem < ptrA.elem:
            ptrB = ptrB.next
            
        # Missing element or overshoot indicates subset validation breakdown
        if ptrB is None or ptrB.elem > ptrA.elem:
            return False
            
        # Target matched successfully; update Set A verification node
        ptrA = ptrA.next
    return True

def run_set_experiments():
    print()    # new line
    print_header("5. Sets: Ordered Subset Verification")
    sizes = [10, 30, 50, 70, 90]
    min_r, max_r, avg_r = [], [], []
    
    # Initialize static evaluation targets
    A_elements = [0, 9]
    setA = OrderedSetLL(A_elements)
    
    for n in sizes:
        ratios = []
        for _ in range(200): # Iterating benchmarks per array scaling size
            # Random sampling without replacement preserving structure requirements
            B_elements = np.random.choice(101, n, replace=False)
            setB = OrderedSetLL(B_elements)
            
            t0 = time.perf_counter()
            Subset(setA, setB)
            ts = time.perf_counter() - t0
            
            t0 = time.perf_counter()
            SubsetFast(setA, setB)
            tf = time.perf_counter() - t0
            
            if tf > 0: ratios.append(ts / tf)
            
        min_r.append(np.min(ratios))
        max_r.append(np.max(ratios))
        avg_r.append(np.mean(ratios))

    plt.figure(figsize=(8, 5))
    plt.plot(sizes, min_r, label='Min Ratio', marker='o')
    plt.plot(sizes, max_r, label='Max Ratio', marker='s')
    plt.plot(sizes, avg_r, label='Avg Ratio', marker='^')
    plt.title("Execution Ratio (Subset / SubsetFast) vs Ordered Set B Size")
    plt.xlabel("Size of Set B (n)")
    plt.ylabel("Execution Ratio")
    plt.legend()
    plt.grid(True)
    plt.savefig("./Subset.jpg")
    plt.close()
    print("    Saved plot to ./Subset.jpg")
    print()



# ==========================================
# Main Execution Trigger
# ==========================================
if __name__ == "__main__":
    t_start = time.time()
    run_moving_averages_experiments()
    run_count_ones_experiments()
    run_recursion_section()
    run_sparse_matrix_experiments()
    run_list_vs_array_deletion()
    run_sharing_matrix()
    run_set_experiments()