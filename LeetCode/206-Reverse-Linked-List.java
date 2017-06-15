/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseList(ListNode head) {
        if(head==null || head.next==null){
            return head;
        }
        ListNode current = head;
        ListNode ret = null;
        while(current.next != null){
            current = current.next;
        }
        ret = current;
        reverseListHelper(head);
        return ret;
        
    }
    public void reverseListHelper(ListNode head){
        ListNode current = head;
        ListNode prev = null;
        while(current.next != null){
            prev = current;
            current = current.next;
        }
        current.next = prev;
        prev.next = null;
        if(head.next == null){
            return;
        }
        reverseListHelper(head);
    }
}