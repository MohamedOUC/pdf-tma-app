<template>
    <div class="search">
        <h2> 🔍 Rechercher un document</h2>
        <form @submit.prevent="search">
            <input v-model="searchTitle" type="text" placeholder="Mot-clé du titre" />
            <button type="submit">Rechercher</button>
        </form>

        <div v-if="results.length">
            <h3>📄 Résultats :</h3>
            <ul>
              <li v-for="doc in results" :key="doc.id">
                <div v-if="editingId !== doc.id">
                  <strong>{{ doc.title }}</strong><br />
                  {{ doc.content }}<br />
                  <button @click="startEdit(doc)">✏️ Modifier</button>
                  <button @click="deleteDocument(doc.id)">🗑️ Supprimer</button>
                </div>
  
                <div v-else>
                  <input v-model="editTitle" placeholder="Titre" />
                  <textarea v-model="editContent" placeholder="Contenu"></textarea><br />
                  <button @click="saveEdit(doc.id)">💾 Enregistrer</button>
                  <button @click="cancelEdit()">❌ Annuler</button>
                </div>
              </li>
            </ul>
        </div>

        <p v-else-if="searched">Aucun résultat trouvé.</p>
    </div>
</template>

<script>
export default {
  data() {
    return {
      searchTitle: '',
      results: [],
      searched: false,
      editingId: null,
      editTitle: '',
      editContent: ''
    };
  },
  methods: {
    async search() {
      this.searched = true;
      const res = await fetch(`http://localhost:8000/documents/search?title=${encodeURIComponent(this.searchTitle)}`);
      if (res.ok) {
        this.results = await res.json();
        if (this.results.length === 0) {
          this.$emit('toast', { message: "Aucun résultat trouvé ❗", type: "error" });
        }
      } else {
        this.$emit('toast', { message: "Erreur recherche ❌", type: "error" });
      }
    },
    async deleteDocument(id) {
      if (confirm("Confirmer la suppression ?")) {
        const res = await fetch(`http://localhost:8000/documents/${id}`, { method: 'DELETE' });
        if (res.ok) {
          this.results = this.results.filter(doc => doc.id !== id)
          this.$emit('toast', { message: "Document supprimé ✅", type: "success" });
        } else {
          this.$emit('toast', { message: "Erreur suppression ❌", type: "error" });
        }
      }
    },
    startEdit(doc) {
      this.editingId = doc.id;
      this.editTitle = doc.title;
      this.editContent = doc.content;
    },
    cancelEdit() {
      this.editingId = null;
      this.editTitle = '';
      this.editContent = '';
    },
    async saveEdit(id) {
      const res = await fetch(`http://localhost:8000/documents/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          title: this.editTitle,
          content: this.editContent
        })
      });
      if (res.ok) {
        const updated = await res.json();
        const index = this.results.findIndex(doc => doc.id === id);
        this.results[index] = updated;
        this.cancelEdit();
        this.$emit('toast', { message: "Document mis à jour ✏️", type: "success" });
      } else {
        this.$emit('toast', { message: "Erreur mise à jour ❌", type: "error" });
      }
    }
  }
}

</script>

<style scoped>
.search {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
}
input {
  width: 70%;
  padding: 6px;
  margin-right: 10px;
}
button {
  padding: 6px 10px;
}
</style>