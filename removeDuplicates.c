void removeDuplicates(struct Node* head)
{
    struct Node* traverse;
    struct Node* after;
    struct Node* del;
    traverse = head;
    after = traverse->next;
    while(after!=NULL)
    {
        if(traverse->data == after->data)
        {
            del = after;
            after = after->next;
            traverse->next = after;
            free(del);
            del = NULL;
        }
        else
        {
            traverse=after;
            after=after->next;
        }
    }
}