
// Definition for a Node.
class Node {
    public int val;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _next) {
        val = _val;
        next = _next;
    }
};


class Solution {
    public Node insert(Node he, int x) {
        Node t = new Node(x);
        t.next = t;
        if (he == null) return t;
        Node ans = he;
        int min = he.val, max = he.val;
        while (he.next != ans) {
            he = he.next;
            min = Math.min(min, he.val);
            max = Math.max(max, he.val);
        }
        if (min == max) {
            t.next = ans.next;
            ans.next = t;
        } else {
            while (!(he.val == max && he.next.val == min)) he = he.next;
            while (!(x <= min || x >= max) && !(he.val <= x && x <= he.next.val)) he = he.next;
            t.next = he.next;
            he.next = t;
        }
        return ans;
    }
}
