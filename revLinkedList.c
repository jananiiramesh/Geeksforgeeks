struct Node* reverseList(struct Node *head)
    {
        struct Node *prev,*cur,*after;
        prev=head;
        cur=head;
        after=head;
        if(cur==head)
        {
            after=cur->next;
            cur->next=NULL;
            prev=cur;
            cur=after;
        }
        while(cur!=NULL)
        {
            after=cur->next;
            cur->next=prev;
            prev=cur;
            cur=after;
        }
        head=prev;
        return head;
    }