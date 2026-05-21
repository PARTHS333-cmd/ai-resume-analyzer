async function analyzeResume() {

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/analyze"
        );

        const data = await response.json();

        console.log(data);

        // ATS Score
        document.getElementById("score").innerText =
            data.ats_score + "%";

        // Matched Skills
        const matchedSkills =
            document.getElementById("matched-skills");

        matchedSkills.innerHTML = "";

        data.matched_skills.forEach(skill => {

            const li = document.createElement("li");

            li.innerText = "✅ " + skill;

            matchedSkills.appendChild(li);
        });

        // Missing Skills
        const missingSkills =
            document.getElementById("missing-skills");

        missingSkills.innerHTML = "";

        data.missing_skills.forEach(skill => {

            const li = document.createElement("li");

            li.innerText = "❌ " + skill;

            missingSkills.appendChild(li);
        });

    } catch (error) {

        console.error("Error:", error);

        alert("Failed to connect to backend API.");
    }
}