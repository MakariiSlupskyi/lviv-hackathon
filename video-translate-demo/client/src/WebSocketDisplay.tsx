import { useEffect, useState } from "react";

// WebSocketDisplay component
export function WebSocketDisplay({ stream_id }: { stream_id: string }) {
  const [imageSrc, setImageSrc] = useState(null);

  useEffect(() => {
    const socket = new WebSocket(`ws://localhost:8000/connect/${stream_id}`);

    socket.onopen = () => {
      console.log("Connected to WebSocket server.");
    };

    socket.onmessage = (event) => {
      // The server sends a base64-encoded JPEG image
      const base64Image = event.data;

      // Update the image source to display the received image
      setImageSrc(`data:image/jpeg;base64,${base64Image}`);
    };

    socket.onerror = (error) => {
      console.error("WebSocket error:", error);
    };

    socket.onclose = () => {
      console.log("WebSocket connection closed.");
    };

    // Cleanup on component unmount
    return () => {
      socket.close();
    };
  }, []);

  return (
    <div>
      {imageSrc ? (
        <img src={imageSrc} className="rounded-xl shadow-xl" alt="Streaming" width="100%" />
      ) : (
        <p>Loading video...</p>
      )}
    </div>
  );
}
