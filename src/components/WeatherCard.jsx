export default function WeatherCard({ data }) {
  if (!data) return null;

  const icon = data.weather[0].icon;

  return (
    <div className="weather-card">
      <h2>{data.name}</h2>

      <img
        src={`https://openweathermap.org/img/wn/${icon}@2x.png`}
        alt="weather"
      />

      <h1>{Math.round(data.main.temp)}°C</h1>
      <p>Humidity: {data.main.humidity}%</p>
      <p>Wind: {data.wind.speed} km/h</p>
    </div>
  );
}
