#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    float data;
    struct node* next;
} Node;

// Function to create a new node
Node* createNode(float data) {
    Node* newNode = (Node*) malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Insert by index
void insertByIndex(Node** head, int index, float val) {
    Node* newNode = createNode(val);
    if (index == 0) {
        newNode->next = *head;
        *head = newNode;
        return;
    }
    Node* temp = *head;
    for (int i = 0; i < index - 1 && temp != NULL; i++)
        temp = temp->next;
    if (temp == NULL) {
        printf("Index out of bounds\n");
        free(newNode);
        return;
    }
    newNode->next = temp->next;
    temp->next = newNode;
}

// Insert by value (end)
void insertByVal(Node** head, float val) {
    Node* newNode = createNode(val);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    Node* temp = *head;
    while (temp->next != NULL)
        temp = temp->next;
    temp->next = newNode;
}

// Delete by index
void deleteByIndex(Node** head, int index) {
    if (*head == NULL) {
        printf("List is empty\n");
        return;
    }
    Node* temp = *head;
    if (index == 0) {
        *head = temp->next;
        free(temp);
        return;
    }
    for (int i = 0; i < index - 1 && temp->next != NULL; i++)
        temp = temp->next;
    if (temp->next == NULL) {
        printf("Index out of bounds\n");
        return;
    }
    Node* toDelete = temp->next;
    temp->next = toDelete->next;
    free(toDelete);
}

// Delete by value
void deleteByVal(Node** head, float val) {
    Node* temp = *head;
    Node* prev = NULL;

    while (temp != NULL && temp->data != val) {
        prev = temp;
        temp = temp->next;
    }
    if (temp == NULL) {
        printf("Value %.2f not found\n", val);
        return;
    }
    if (prev == NULL)
        *head = temp->next;
    else
        prev->next = temp->next;

    free(temp);
}

// Print list
void printList(Node* head) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    Node* temp = head;
    while (temp != NULL) {
        printf("%.2f -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

// Search
int search(Node* head, float val) {
    int index = 0;
    while (head != NULL) {
        if (head->data == val)
            return index;
        head = head->next;
        index++;
    }
    return -1;
}

// Is empty
int isEmpty(Node* head) {
    return head == NULL ? 1 : 0;
}

// Main menu
int main() {
    Node* head = NULL;
    int choice, index;
    float val;

    do {
        printf("\n--- Linked List Menu ---\n");
        printf("1. Insert By Index\n2. Insert By Value\n3. Delete By Index\n");
        printf("4. Delete By Value\n5. Print List\n6. Search\n7. Is Empty\n8. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter index and value: ");
                scanf("%d %f", &index, &val);
                insertByIndex(&head, index, val);
                break;
            case 2:
                printf("Enter value: ");
                scanf("%f", &val);
                insertByVal(&head, val);
                break;
            case 3:
                printf("Enter index: ");
                scanf("%d", &index);
                deleteByIndex(&head, index);
                break;
            case 4:
                printf("Enter value: ");
                scanf("%f", &val);
                deleteByVal(&head, val);
                break;
            case 5:
                printList(head);
                break;
            case 6:
                printf("Enter value to search: ");
                scanf("%f", &val);
                index = search(head, val);
                if (index != -1)
                    printf("Value found at index %d\n", index);
                else
                    printf("Value not found\n");
                break;
            case 7:
                if (isEmpty(head))
                    printf("List is empty\n");
                else
                    printf("List is not empty\n");
                break;
            case 8:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice!\n");
        }
    } while (choice != 8);

    return 0;
}
