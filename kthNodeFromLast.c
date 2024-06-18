int count(struct Node* head)
{
    struct Node* traverse=head;
    int count=0;
    while(traverse!=NULL)
    {
        count++;
        traverse=traverse->next;
    }
    return count;
}
int getNthFromLast(struct Node *head, int n)
{
    int nodes=count(head);
    int value=(nodes-n)+1;
    struct Node* cur=head;
    int count=1;
    while(cur!=NULL && count!=value)
    {
        count++;
        cur=cur->next;
    }
    if(cur!=NULL && count==value)
    {
        return cur->data;
    }
    else
    {
        return -1;
    }
}