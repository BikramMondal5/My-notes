#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Structure to hold a data point
typedef struct {
    double x;      // Feature 1
    double y;      // Feature 2
    int label;     // Class label (e.g., 0 or 1)
} Point;

// Function to calculate Euclidean distance
double distance(Point a, Point b) {
    return sqrt((a.x - b.x) * (a.x - b.x) +
                (a.y - b.y) * (a.y - b.y));
}

// KNN classification
int knn(Point dataset[], int dataSize, Point query, int k) {
    double *distances = (double *)malloc(dataSize * sizeof(double));
    int *labels = (int *)malloc(dataSize * sizeof(int));

    // Calculate distances to all points
    for (int i = 0; i < dataSize; i++) {
        distances[i] = distance(dataset[i], query);
        labels[i] = dataset[i].label;
    }

    // Sort by distance (simple bubble sort for clarity)
    for (int i = 0; i < dataSize - 1; i++) {
        for (int j = i + 1; j < dataSize; j++) {
            if (distances[i] > distances[j]) {
                double tempDist = distances[i];
                distances[i] = distances[j];
                distances[j] = tempDist;

                int tempLabel = labels[i];
                labels[i] = labels[j];
                labels[j] = tempLabel;
            }
        }
    }

    // Count votes for the first k neighbors
    int count0 = 0, count1 = 0;
    for (int i = 0; i < k; i++) {
        if (labels[i] == 0)
            count0++;
        else
            count1++;
    }

    free(distances);
    free(labels);

    return (count1 > count0) ? 1 : 0;
}

int main() {
    // Sample dataset (x, y, label)
    Point dataset[] = {
        {1.0, 2.0, 0},
        {1.5, 1.8, 0},
        {5.0, 8.0, 1},
        {6.0, 9.0, 1},
        {1.2, 0.8, 0},
        {7.0, 10.0, 1}
    };
    int dataSize = sizeof(dataset) / sizeof(dataset[0]);
    printf("Dataset size: %d\n", dataSize);
    Point query = {2.0, 3.0}; // Point to classify
    int k;
    printf("Enter the value of k: ");
    scanf("%d",&k);
    
    

    int result = knn(dataset, dataSize, query, k);

    printf("Predicted class for (%.1f, %.1f) is: %d\n",
           query.x, query.y, result);

    return 0;
}
