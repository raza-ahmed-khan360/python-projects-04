MAX_TERM_VALUE: int = 10000

def main():
    curr_term = 0
    nxt_term = 1
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)
        term_after_nxt = curr_term + nxt_term
        curr_term = nxt_term
        nxt_term = term_after_nxt

if __name__ == "__main__":
    main()