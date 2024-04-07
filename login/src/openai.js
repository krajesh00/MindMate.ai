export async function signUp(firstName, lastName, username, password, age, email) {
    let signUpObj = {
        firstName: firstName,
        lastName: lastName,
        username: username,
        password: password,
        age: age,
        email: email
    }

    try {
            const response = await fetch('http://localhost:8000/signup/', { // Replace with your actual endpoint URL
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(signUpObj)
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error:', error);
    }

}

export default async function login(username, password) {
    let loginObj = {
        username: username,
        password: password
    }

    try {
            const response = await fetch('http://localhost:8000/login/', { // Replace with your actual endpoint URL
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(loginObj)
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error:', error);
    }

}

