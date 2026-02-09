// JavaScript Example: Working with a User Profile

// 1. Variables and basic data types
const userName = "Alice";
const age = 28;
const isStudent = false;

console.log(`Welcome, ${userName}! You are ${age} years old.`);

// 2. Arrays and loops
const hobbies = ["reading", "gaming", "cooking"];
console.log("\nHobbies:");
hobbies.forEach((hobby, index) => {
  console.log(`  ${index + 1}. ${hobby}`);
});

// 3. Objects (like a data container)
const person = {
  name: "Alice",
  age: 28,
  city: "New York",
  greet: function() {
    return `Hi, I'm ${this.name} from ${this.city}!`;
  }
};

console.log("\n" + person.greet());

// 4. Functions and conditional logic
function calculateAgeCategory(age) {
  if (age < 13) return "Child";
  if (age < 18) return "Teen";
  if (age < 65) return "Adult";
  return "Senior";
}

const category = calculateAgeCategory(person.age);
console.log(`Age category: ${category}`);

// 5. Working with numbers
const scores = [85, 92, 78, 95, 88];
const average = scores.reduce((sum, score) => sum + score, 0) / scores.length;
console.log(`\nAverage score: ${average.toFixed(1)}`);

// 6. Conditional and simple logic
console.log("\nScore analysis:");
scores.forEach(score => {
  const grade = score >= 90 ? "A" : score >= 80 ? "B" : "C";
  console.log(`  Score ${score}: ${grade}`);
});
