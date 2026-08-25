class Solution {
public:
    ListNode* reverse(ListNode* head) {
        ListNode* prev = nullptr;
        while (head) {
            ListNode* next = head->next;
            head->next = prev;
            prev = head;
            head = next;
        }
        return prev;
    }

    bool isPalindrome(ListNode* head) {
        if (!head || !head->next)
            return true;

        // Find middle
        ListNode *slow = head, *fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Reverse second half
        ListNode* secondHalf = reverse(slow->next);

        // Compare both halves
        ListNode* firstHalf = head;
        ListNode* temp = secondHalf;

        while (temp) {
            if (firstHalf->val != temp->val)
                return false;
            firstHalf = firstHalf->next;
            temp = temp->next;
        }

        return true;
    }
};