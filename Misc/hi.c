#include <stdio.h>
#include <stdlib.h>

int main(){
    char* original_word = "zzzzzane";
    
    
    int i = 0;
    
    int pos = 0;
    int l = 5;
    char *resultant_word = malloc(l + 1);

    while (i < l) {
        resultant_word[i] = original_word[pos + i];
        i++;
    }
    
    resultant_word[i] = '\0';  


// ---------------

    i = 0;
    pos = 5;
    l = 8 - pos;
    char *postsplit = malloc(l + 1);

    while (i < l) {
        postsplit[i] = original_word[pos + i];
        i++;
    }
    
    postsplit[i] = '\0';  

    printf("%s%say\n",resultant_word, postsplit);

}