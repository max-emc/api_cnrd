// Import Firebase functions
import { initializeApp } from "firebase/app";
import { getFirestore, doc, setDoc, getDoc } from "firebase/firestore";

// Configuration Firebase
const firebaseConfig = {
  apiKey: "AIzaSyAZX87nTYKM8uLRWYxqw8s74qkO4Wnhg-I",
  authDomain: "test-2edff.firebaseapp.com",
  projectId: "test-2edff",
  storageBucket: "test-2edff.firebasestorage.app",
  messagingSenderId: "689206193044",
  appId: "1:689206193044:web:1890e2f9db67dc4d0abd81",
  measurementId: "G-QZDX8MS9LJ",
};

// Initialiser Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

const container = document.getElementById("tutorials");

const default_data = {
  boat_game: [""],
  infiltration: [""],
  parachut_drop: [],
  flag_game: [],
  rebuild_house: [],
  ressource_game: [],
  quiz: [],
  finances: [],
};

// Charger les données de Firebase
async function loadData() {
  const docRef = doc(db, "tutorials", "gameData");
  const docSnap = await getDoc(docRef);

  if (docSnap.exists()) {
    return docSnap.data();
  } else {
    console.log("Aucune donnée trouvée, utilisation des données par défaut.");
    return default_data;
  }
}

// Fonction pour convertir BBCode en HTML
function bbcodeToHtml(bbcode) {
  return bbcode
    .replace(/\[center\](.*?)\[\/center\]/g, "<center>$1</center>")
    .replace(/\[b\](.*?)\[\/b\]/g, "<strong>$1</strong>")
    .replace(/\[i\](.*?)\[\/i\]/g, "<em>$1</em>")
    .replace(/\[u\](.*?)\[\/u\]/g, "<u>$1</u>")
    .replace(/\[url=(.*?)\](.*?)\[\/url\]/g, '<a href="$1">$2</a>')
    .replace(/\[img\](.*?)\[\/img\]/g, '<img src="$1" alt="Image">')
    .replace(
      /\[color=(.*?)\](.*?)\[\/color\]/g,
      '<span style="color:$1;">$2</span>',
    );
}

// Mettre à jour l'interface avec les données
async function updateUI() {
  let tutorials = await loadData();

  Object.entries(tutorials).forEach(([key, value]) => {
    const div = document.createElement("div");
    div.className = "tutorial";

    const title = document.createElement("h1");
    title.textContent = key.replace("_", " ");

    const textarea = document.createElement("textarea");
    textarea.id = key;
    textarea.value = value.join("\n");

    const bbcodeOutput = document.createElement("p");
    bbcodeOutput.innerHTML = value
      .map((line) => bbcodeToHtml(line))
      .join("<br>");

    textarea.addEventListener("input", () => {
      const lines = textarea.value.split("\n");
      bbcodeOutput.innerHTML = lines
        .map((line) => bbcodeToHtml(line))
        .join("<br>");
    });

    div.appendChild(title);
    div.appendChild(textarea);
    div.appendChild(bbcodeOutput);
    container.appendChild(div);
  });
}

// Sauvegarder dans Firebase Firestore
async function save() {
  const data = getData();

  try {
    await setDoc(doc(db, "tutorials", "gameData"), data);
    showMessage("Fichier enregistré avec succès !");
  } catch (e) {
    console.error("Erreur lors de l'enregistrement dans Firebase : ", e);
  }
}

// Fonction pour récupérer les données
function getData() {
  let data = {};
  const textareas = document.querySelectorAll("textarea");

  textareas.forEach((textarea) => {
    data[textarea.id] = textarea.value.split("\n");
  });

  return data;
}

// Afficher un message de confirmation
function showMessage(message) {
  const messageDiv = document.createElement("div");
  messageDiv.textContent = message;
  messageDiv.style.position = "fixed";
  messageDiv.style.bottom = "20px";
  messageDiv.style.right = "20px";
  messageDiv.style.backgroundColor = "#4CAF50";
  messageDiv.style.color = "white";
  messageDiv.style.padding = "10px";
  messageDiv.style.borderRadius = "5px";
  messageDiv.style.zIndex = "1000";

  document.body.appendChild(messageDiv);

  setTimeout(() => {
    messageDiv.remove();
  }, 3000);
}

// Charger les données au démarrage et initialiser l'interface
updateUI();

// Ajouter des événements de sauvegarde
document.getElementById("saveButton").addEventListener("click", save);
document.addEventListener("keydown", (event) => {
  if (event.ctrlKey && event.key === "s") {
    event.preventDefault();
    save();
  }
});
