// Exercise 2.4: Fetch and Display API Data
const API_URL = "https://jsonplaceholder.typicode.com/users";

// TODO 1: grab loader, errorBox, errorMessage, retryBtn, userGrid

// TODO 2: showLoading(), showError(message), showSuccess()
//         exactly ONE of loader / errorBox / userGrid is visible at a time (use the hidden attribute)

// TODO 3: initials(name) -> "LG" for "Leanne Graham"

// TODO 4: createCard(user) -> build the card with createElement + textContent:
//         avatar (initials), name, email as mailto: link, phone as tel: link, company name badge

// TODO 5: renderUsers(users) -> clear the grid, append one card per user

// TODO 6: async function loadUsers()
//         showLoading(); try { fetch; check response.ok; response.json(); render; showSuccess() }
//         catch (err) { showError(err.message) }

// TODO 7: retryBtn click -> loadUsers()

// TODO 8: call loadUsers() when the page loads
