import { useEffect } from "react";
import useApi from "../../hooks/useApi";
import "./index.css";
import VerifiedIcon from "../../assets/verified-icon.png";

export default function ArtistaCover({ artistId }: { artistId: number }) {
  const { artist, fetchArtistById, loading, error } = useApi();

  // Fetch the artist by ID when the component mounts
  useEffect(() => {
    fetchArtistById(artistId);
  }, [artistId, fetchArtistById]);

  // Handle loading and error states
  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;
  if (!artist) return <p>No artist data available.</p>;

  return (
    <div className="container-artists">
      <img src={artist.banner} alt="Artist Banner" className="artist-banner" />
      {artist.isVerified && (
        <div className="verified-artist">
          <img className="verified-icon" src={VerifiedIcon} alt="Verified Icon" />
          <p>Artista verificado</p>
        </div>
      )}
    </div>
  );
}