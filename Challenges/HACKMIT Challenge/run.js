allLetters = "IHOCHOHCHHOHHCHCHO"
userId = "6720052"

const response = await axios.post(
    "https://hexhunt.hackmit.org/solve_hex_hunt",
    { letters: allLetters, userId }
  );