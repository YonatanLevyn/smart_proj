document.addEventListener("DOMContentLoaded", () => {
    const introductionForm = document.getElementById("introduction-form");
    const introductionInput = document.getElementById("introduction");
    const introductionDisplay = document.getElementById("introduction-display");
  
    introductionForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const introduction = introductionInput.value;
  
      // Send the update request.
      const response = await fetch(introductionForm.action, {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          "X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0].value,
        },
        body: new URLSearchParams({ introduction }),
      });
  
      if (response.ok) {
        // Update the introduction display.
        introductionDisplay.textContent = introduction;
        introductionDisplay.style.display = "block";
  
        // Hide the input box and the form.
        introductionForm.style.display = "none";
      } else {
        // Handle errors here, if any.
        console.error("Error updating introduction");
      }
    });
  });
  