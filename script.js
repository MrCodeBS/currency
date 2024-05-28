function toggleDarkMode() {
    const body = document.body;
    body.classList.toggle('dark-mode');

    //Store the user's preference in localStoreage
    const isDarkMode = body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDarkMode);
}
//function to set the initial dark mode state when the page loads
function setDarkModeFromLocalStorage() {
    const isDarkMode = localStorage.getItem('darkMode') === true;
    const body = document.body;
    if (isDarkMode){
        body.classList.add("dark-mode");
    }else{
        body.classList.remove("dark-mode");
    }
}

//Call the function to set  the initial dark mode state
setDarkModeFromLocalStorage();

const conversionRates = {
    VBUCKS: 0.0097924 // Fortnite V-Bucks to CHF rate
};

