#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct oto {
    char buffer[100];
    struct oto* next;
    int sayi;
} otopark;

otopark* start = NULL;

void newcar();
void deletecar();
void listele();
void adjustcount();

int main() {
    int choice;
    while (1) {
        printf("1. Yeni Arac Girisi\n");
        printf("2. Arac Cikisi\n");
        printf("3. Guncel Araclari Listeleme\n");
        printf("4. Cikis\n\n");
        printf("Seciminizi giriniz: ");
        scanf("%d", &choice);
        getchar();

        switch (choice) {
            case 1:
                newcar();
                break;
            case 2:
                deletecar();
                break;
            case 3:
                listele();
                break;
            case 4:
                exit(0);
            default:
                printf("Gecersiz secim\n");
        }
    }
    return 0;
}

void newcar() {
    int girissaati;
    char plaka[100];
    otopark* add;

    printf("Otoparka giris saati: ");
    scanf("%d", &girissaati);
    getchar();

    printf("Aracin plakasini giriniz: ");
    fgets(plaka, 100, stdin);
    plaka[strcspn(plaka, "\n")] = 0;

    add = (otopark*)malloc(sizeof(otopark));
    strcpy(add->buffer, plaka);
    add->sayi = (start == NULL) ? 1 : start->sayi + 1;
    add->next = start;
    start = add;
}

void deletecar() {
    int x;
    otopark *del, *temp;

    if (start == NULL) {
        printf("Otopark bos\n");
        return;
    }

    printf("Kacinci siradaki arac cikacak: ");
    scanf("%d", &x);

    del = start;

    if (del->sayi == x) {
        start = start->next;
        free(del);
        adjustcount();
        return;
    }

    temp = start;
    while (temp->next != NULL) {
        if (temp->next->sayi == x) {
            otopark* target = temp->next;
            temp->next = target->next;
            free(target);
            adjustcount();
            return;
        }
        temp = temp->next;
    }

    printf("Arac bulunamadi\n");
}

void listele() {
    otopark* temp = start;

    if (temp == NULL) {
        printf("Otopark bos\n");
        return;
    }

    while (temp != NULL) {
        printf("%d.) %s\n", temp->sayi, temp->buffer);
        temp = temp->next;
    }
}

void adjustcount() {
    otopark* temp = start;
    int i = 1;

    while (temp != NULL) {
        temp->sayi = i;
        i++;
        temp = temp->next;
    }
}
