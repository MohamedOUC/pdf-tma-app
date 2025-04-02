<template>
  <main>
    <h1>📁 Tableau de bord</h1>
    <DocumentForm />
    <hr />
    <DocumentSearch />
  </main>
</template>

<script>
import DocumentForm from '@/components/DocumentForm.vue';
import DocumentSearch from '@/components/DocumentSearch.vue';

export default {
  components: {
    DocumentForm,
    DocumentSearch
  }
};
</script>