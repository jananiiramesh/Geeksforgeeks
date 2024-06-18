int isPalindrome(char  S[])
    {
        int len=strlen(S);
        if(len%2==0)
        {
            //int half=len/2;
            int i=0;
            //int j=half;
            int k=(len-1);
            while(k>=(len/2))
            {
                if(S[i]!=S[k])
                {
                    return 0;
                }
                i++;
                k--;
            }
            return 1;
        }
        else
        {
            int half=len/2;
            int i=0;
            int k=(len-1);
            while(i!=half)
            {
                if(S[i]!=S[k])
                {
                    return 0;
                }
                i++;
                k++;
            }
            return 1;
        }
    }