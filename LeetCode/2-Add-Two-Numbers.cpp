/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    //adds up the numbers in the two lists
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if(l1 == nullptr && l2 != nullptr)
            l1 = new ListNode(0);
        else if(l2 == nullptr && l1 != nullptr)
            l2 = new ListNode(0);
        else if(l2 == nullptr && l1 == nullptr)
            return nullptr;
        int sum = l1->val + l2->val;
        ListNode* root = new ListNode(sum);
        root->next = addTwoNumbers(l1->next, l2->next);
        carryOut(root);
        return root;
    }
    //fixes numbers with multiple digits
    void carryOut(ListNode* root){
        if(root == nullptr){
            return;
        }
        if(root->val < 10){
            carryOut(root->next);
            return;
        }
        int carry = root->val/10;
        root->val -= carry*10;
        if(root->next){
            root->next->val += carry;
        }
        else{
            root->next = new ListNode(carry);
        }
        carryOut(root->next);
        return;
    }
};