// Power function to return (a^b) % p
function power(a, b, p) {
    let result = 1;
    a = a % p; // Reduce base modulo p
    while (b > 0) {
        // If b is odd, multiply a with result
        if (b % 2 === 1) {
            result = (result * a) % p;
        }
        // Now b must be even, so divide by 2
        b = Math.floor(b / 2);
        a = (a * a) % p; // Square a
    }
    return result;
}

// Main Diffie-Hellman Key Exchange Logic
function diffieHellman() {
    let outputDiv = document.getElementById("output");

    // Publicly known values
    let P = 23; // Prime number
    let G = 9;  // Primitive root modulo P

    // Private keys (chosen by Alice and Bob)
    let a = 4; // Alice's private key
    let b = 3; // Bob's private key

    // Compute public keys
    let x = power(G, a, P); // Alice's public key
    let y = power(G, b, P); // Bob's public key

    // Compute shared secret keys
    let ka = power(y, a, P); // Alice's secret key
    let kb = power(x, b, P); // Bob's secret key

    // Display output
    let output = `
        <p>The value of P: ${P}</p>
        <p>The value of G: ${G}</p>
        <p>The private key a for Alice: ${a}</p>
        <p>The private key b for Bob: ${b}</p>
        <p>Secret key for Alice: ${ka}</p>
        <p>Secret key for Bob: ${kb}</p>
    `;

    outputDiv.innerHTML = output;
}

// Run the function
diffieHellman();
