#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node {
    float data;
    struct node *next;
} Node;

Node* insertByIndex(Node **head, int index, float val) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = val;
    if (index == 0) {
        newNode->next = *head;
        *head = newNode;
        return *head;
    }
    Node *current = *head;
    for (int i = 0; i < index - 1 && current != NULL; i++) {
        current = current->next;
    }
    if (current == NULL) return *head;
    newNode->next = current->next;
    current->next = newNode;
    return *head;
}

Node* insertByVal(Node **head, float val) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = val;
    newNode->next = *head;
    *head = newNode;
    return *head;
}

Node* deleteByIndex(Node **head, int index) {
    if (*head == NULL) return *head;
    if (index == 0) {
        Node *temp = *head;
        *head = (*head)->next;
        free(temp);
        return *head;
    }
    Node *current = *head;
    for (int i = 0; i < index - 1 && current != NULL; i++) {
        current = current->next;
    }
    if (current == NULL || current->next == NULL) return *head;
    Node *temp = current->next;
    current->next = current->next->next;
    free(temp);
    return *head;
}

Node* deleteByVal(Node **head, float val) {
    if (*head == NULL) return *head;
    if ((*head)->data == val) {
        Node *temp = *head;
        *head = (*head)->next;
        free(temp);
        return *head;
    }
    Node *current = *head;
    while (current->next != NULL && current->next->data != val) {
        current = current->next;
    }
    if (current->next == NULL) return *head;
    Node *temp = current->next;
    current->next = current->next->next;
    free(temp);
    return *head;
}

void printlist(Node **head) {
    Node *current = *head;
    while (current != NULL) {
        printf("%.2f ", current->data);
        current = current->next;
    }
    printf("\n");
}

int search(Node *head, float val) {
    Node *current = head;
    int index = 0;
    while (current != NULL) {
        if (current->data == val) return index;
        current = current->next;
        index++;
    }
    return -1; 
}

// Search duplicate elements and print their indexes
void searchDuplicates(Node *head) {
    int indexOuter = 0;
    bool found = false;
    for (Node *outer = head; outer != NULL; outer = outer->next) {
        int indexInner = 0;
        for (Node *inner = head; inner != NULL; inner = inner->next) {
            if (indexInner != indexOuter && inner->data == outer->data) {
                printf("Duplicate value %.2f found at indexes %d and %d\n", outer->data, indexOuter, indexInner);
                found = true;
                break; // Avoid printing same duplicate multiple times
            }
            indexInner++;
        }
        indexOuter++;
    }
    if (!found) {
        printf("No duplicates found.\n");
    }
}

// Fixed deletedublicate function
void deletedublicate(Node **head, float val) {
    Node *current = *head;
    Node *prev = NULL;
    while (current != NULL) {
        if (current->data == val) {
            Node *temp = current;
            if (prev == NULL) {
                *head = current->next; // deleting head
            } else {
                prev->next = current->next;
            }
            current = current->next;
            free(temp);
        } else {
            prev = current;
            current = current->next;
        }
    }
}

bool isEmpty(Node **head) {
    return *head == NULL;
}

int main() {
    Node *head = NULL;
    int choice, index;
    float val;

    do {
        printf("\n1. Insert by index\n");
        printf("2. Insert by value\n");
        printf("3. Delete by index\n");
        printf("4. Delete by value\n");
        printf("5. Print list\n");
        printf("6. Search\n");
        printf("7. Check if empty\n");
        printf("8. Delete duplicate\n");
        printf("9. Search duplicates and print indexes\n");
        printf("0. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter index and value: ");
                scanf("%d %f", &index, &val);
                head = insertByIndex(&head, index, val);
                break;
            case 2:
                printf("Enter value: ");
                scanf("%f", &val);
                head = insertByVal(&head, val);
                break;
            case 3:
                printf("Enter index: ");
                scanf("%d", &index);
                head = deleteByIndex(&head, index);
                break;
            case 4:
                printf("Enter value: ");
                scanf("%f", &val);
                head = deleteByVal(&head, val);
                break;
            case 5:
                printlist(&head);
                break;
            case 6:
                printf("Enter value to search: ");
                scanf("%f", &val);
                {
                    int result = search(head, val);
                    if (result == -1) printf("Value not found\n");
                    else printf("Value found at index %d\n", result);
                }
                break;
            case 7:
                if (isEmpty(&head)) printf("List is empty\n");
                else printf("List is not empty\n");
                break;
            case 8:
                printf("Enter duplicate value to delete: ");
                scanf("%f", &val);
                deletedublicate(&head, val);
                break;
            case 9:
                searchDuplicates(head);
                break;
            case 0:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice\n");
        }
    } while (choice != 0);

    return 0;
}
