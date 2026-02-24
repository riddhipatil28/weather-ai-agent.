import { useState } from "react";

export default function SearchBar({ onSearch }) {
  const [city, setCity] = useState("");

  const handleClick = () => {
    onSearch(city);
    setCity("");
  };

  return (
    <div style={{ marginBottom: "20px" }}>
      <input
        value={city}
        onChange={(e) => setCity(e.target.value)}
        placeholder="Enter city"
        style={{
          padding: "10px",
          borderRadius: "8px",
          border: "none",
          outline: "none",
          marginRight: "10px",
        }}
      />

      <button
        onClick={handleClick}
        style={{
          padding: "10px 15px",
          borderRadius: "8px",
          border: "none",
          background: "#222",
          color: "white",
          cursor: "pointer",
        }}
      >
        Search
      </button>
    </div>
  );
}
