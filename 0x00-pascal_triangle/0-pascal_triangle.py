function pascalTriangle(n) {
    if (n <= 0) {
        return [];
    }
    
    const triangle = [];
    
    for (let i = 0; i < n; i++) {
        const row = new Array(i + 1).fill(1); // Start with a row of 1s
        
        for (let j = 1; j < i; j++) {
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]; // Sum of two elements above
        }
        
        triangle.push(row);
    }
    
    return triangle;
}

