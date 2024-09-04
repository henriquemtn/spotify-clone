import { useState, useEffect } from 'react';
import api from '../lib/axios';
import { Artist } from '../types/types';

const useApi = () => {
  const [artists, setArtists] = useState<Artist[]>([]);
  const [artist, setArtist] = useState<Artist | null>(null); // State for a single artist
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // Fetch all artists
  const fetchArtists = async () => {
    try {
      setLoading(true);
      const response = await api.get<Artist[]>('/api/artists/');
      setArtists(response.data);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Fetch artist by ID
  const fetchArtistById = async (id: number) => {
    try {
      setLoading(true);
      const response = await api.get<Artist>(`/api/artists/${id}/`);
      setArtist(response.data); // Set the entire artist object
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchArtists();
  }, []);

  return { artists, artist, loading, error, fetchArtistById };
};

export default useApi;
