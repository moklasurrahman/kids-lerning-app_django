const quizContainer = document.getElementById('quiz');
const resultsContainer = document.getElementById('results');
const submitButton = document.getElementById('submit');
(function(){
    // Functions
    function buildQuiz(){
      // variable to store the HTML output
      const output = [];
  
      // for each question...
      myQuestions.forEach(
        (currentQuestion, questionNumber) => {
  
          // variable to store the list of possible answers
          const answers = [];
  
          // and for each available answer...
          for(letter in currentQuestion.answers){
  
            // ...add an HTML radio button
            answers.push(
              `<label>
                <input type="radio" name="question${questionNumber}" value="${letter}">
                ${letter} :
                ${currentQuestion.answers[letter]}
              </label>`
            );
          }
  
          // add this question and its answers to the output
          output.push(
            `<div class="slide">
              <div class="question"> ${currentQuestion.question} </div>
              <div class="answers"> ${answers.join("")} </div>
            </div>`
          );
        }
      );
  
      // finally combine our output list into one string of HTML and put it on the page
      quizContainer.innerHTML = output.join('');
    }
  
    function showResults(){
  
      // gather answer containers from our quiz
      const answerContainers = quizContainer.querySelectorAll('.answers');
  
      // keep track of user's answers
      let numCorrect = 0;
  
      // for each question...
      myQuestions.forEach( (currentQuestion, questionNumber) => {
  
        // find selected answer
        const answerContainer = answerContainers[questionNumber];
        const selector = `input[name=question${questionNumber}]:checked`;
        const userAnswer = (answerContainer.querySelector(selector) || {}).value;
  
        // if answer is correct
        if(userAnswer === currentQuestion.correctAnswer){
          // add to the number of correct answers
          numCorrect++;
  
          // color the answers green
          answerContainers[questionNumber].style.color = 'lightgreen';
        }
        // if answer is wrong or blank
        else{
          // color the answers red
          answerContainers[questionNumber].style.color = 'red';
        }
      });
  
      // show number of correct answers out of total
      resultsContainer.innerHTML = `${numCorrect}  out of ${myQuestions.length}`;
    }
  
    function showSlide(n) {
      slides[currentSlide].classList.remove('active-slide');
      slides[n].classList.add('active-slide');
      currentSlide = n;
      if(currentSlide === 0){
        previousButton.style.display = 'none';
      }
      else{
        previousButton.style.display = 'inline-block';
      }
      if(currentSlide === slides.length-1){
        nextButton.style.display = 'none';
        submitButton.style.display = 'inline-block';
      }
      else{
        nextButton.style.display = 'inline-block';
        submitButton.style.display = 'none';
      }
    }
  
    function showNextSlide() {
      showSlide(currentSlide + 1);
    }
  
    function showPreviousSlide() {
      showSlide(currentSlide - 1);
    }
  
    // Variables
    const quizContainer = document.getElementById('quiz');
    const resultsContainer = document.getElementById('results');
    const submitButton = document.getElementById('submit');
    const myQuestions = [
      {
        question: "নিচের কোনটি ট্রাক ?",
        answers: {
          a: "🚌",
          b: "🛺",
          c: "🚚",
          d: "🏍"
        },
        correctAnswer: "c"
      },
      {
        question: "৫ এর পরে কোন সংখ্যা কি আসে ?",
        answers: {
          a: "৭",   
          b: "৬",
          c: "১০",
          d: "15"

        },
        correctAnswer: "b"
      },
      {
        question: "কোন প্রাণীকে বনের রাজা বলা হয়?",
        answers: {
          a: "কুকুর 🐕",
          b: "বিড়াল 🐈 ",
          c: "হাতি 🐘",
          d: "সিংহ 🦁"
        },
        correctAnswer: "d"
      },
      {
        question: "গরু কি দেয় ?",
        answers: {
          a: "দুধ 🍼",
          b: "পানি 🚰",
          c: "জুস 🍷",
          d: "কোনটি নয়"
        },
        correctAnswer: "a"
      },
      {
        question: "ছাগলের কয়টি পা আছে?🐐",
        answers: {
          a: "৬",
          b: "৩",
          c: "২",
          d: "৪"
        },
        correctAnswer: "d"
      },
      {
        question: "আমাদের দুই হাতে কয়টি আঙ্গুল আছে ? 🧤",
        answers: {
          a: "৬",
          b: "১০",
          c: "15",
          d: "5"
        },
        correctAnswer: "b"
      },
      {
        question: "কত দিনে এক বছর?",
        answers: {
          a: "২০০",
          b: "৪০০",
          c: "৩৬৫",
          d: "৭০"
        },
        correctAnswer: "c"
      },
      {
        question: "কোন প্রাণীকে মরুভূমির জাহাজ বলা হয় ??",
        answers: {
          a: "উট 🐫",
          b: " ছাগল  🐐",
          c: "ঘোড়া 🐎",
          d: "কোনটি নয়"
        },
        correctAnswer: "a"
      },
      {
        question: "কোন প্রাণী দাঁড়িয়ে ঘুমায়?",
        answers: {
          a: "ভেড়া 🐏",
          b: "ঘোড়া 🐎",
          c: "ছাগল 🐐",
          d: "উট 🐫"
        },
        correctAnswer: "b"
      },
      {
        question: "আমাদের জাতীয় পাখির নাম কি?",
        answers: {
          a: "ঈগল পাখির🦅",
          b: "টিয়া পাখির🦜",
          c: "দোয়েল পাখির",
          d: "ময়না পাখির"
        },
        correctAnswer: "c"
      },
    ];
  
    // Kick things off
    buildQuiz();
  
    // Pagination
    const previousButton = document.getElementById("previous");
    const nextButton = document.getElementById("next");
    const slides = document.querySelectorAll(".slide");
    let currentSlide = 0;
  
    // Show the first slide
    showSlide(currentSlide);
  
    // Event listeners
    submitButton.addEventListener('click', showResults);
    previousButton.addEventListener("click", showPreviousSlide);
    nextButton.addEventListener("click", showNextSlide);
  })();
  