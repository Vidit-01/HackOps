// src/App.js
import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [items, setItems] = useState([]);

  const handleFileChange = (e) => setFile(e.target.files[0]);

  const handleUpload = async () => {
    if (!file) return alert("Please select a file");

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://localhost:5000/reccomend", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      console.log(response.data);
      setItems(response.data);
      console.log(typeof response)
    } catch (err) {
      console.error(err);
      alert("Upload failed");
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-6">
      <h1 className="text-3xl font-bold mb-6">PDF Upload App</h1>

      <div className="flex gap-4 mb-6">
        <input
          type="file"
          accept="application/pdf"
          onChange={handleFileChange}
          className="border border-gray-300 p-2 rounded"
        />
        <button
          onClick={handleUpload}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Upload
        </button>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 w-full max-w-5xl">
        {items.map((item,index) => (
          <div
            key={item}
            className="bg-white shadow rounded p-4 hover:shadow-md transition"
          >
            <h3 className="text-xl font-semibold mb-2">{index}</h3>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
