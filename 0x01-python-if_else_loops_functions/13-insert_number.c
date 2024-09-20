#include <stdlib.h>

typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node = malloc(sizeof(listint_t));
    if (new_node == NULL) {
        return NULL; // Return NULL if memory allocation fails
    }

    new_node->n = number;
    new_node->next = NULL;

    // If the list is empty or the new number should be inserted at the head
    if (*head == NULL || (*head)->n >= number) {
        new_node->next = *head; // Point to the current head
        *head = new_node;       // Update head to new node
        return new_node;
    }

    // Find the correct position to insert the new node
    listint_t *current = *head;
    while (current->next != NULL && current->next->n < number) {
        current = current->next;
    }

    // Insert the new node
    new_node->next = current->next; // Point to the next node
    current->next = new_node;       // Link current node to new node

    return new_node; // Return the address of the new node
}
