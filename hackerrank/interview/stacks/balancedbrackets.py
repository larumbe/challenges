# https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

def isBalanced(s):
    opbr = "{[("                # opening brackets
    clbr = "}])"                # closing brackets
    st = []
    for c in s:
        if c in opbr:
            st.append(c)
        elif c in clbr:
            to = st.pop()
            if opbr[clbr.index(c)] is not to:
                return
         
    if (st == []):
        print("YES")
    else:
        print("NO")
    return
