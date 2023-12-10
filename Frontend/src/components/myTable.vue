<template>
    <div class="container">
        <div class="card">
            <DataTable v-model:filters="filters" stripedRows  :value="products" showGridlines tableStyle="min-width: 50rem" paginator
                :rows="10" :rowsPerPageOptions="[5, 10, 20, 50]">
                <template #header>
                    <InputText v-model="filters['global'].value" placeholder="suchen ..." />
                </template>
                <template #empty> Keine Daten gefunden</template>
                <template #loading> Laden.. </template>
                <Column field="name" header="Name" sortable></Column>
                <Column field="email" header="Email" sortable></Column>
                <Column field="age" header="Age" sortable></Column>
                <Column field="birthdate" header="Birthdate" sortable></Column>
            </DataTable>
        </div>
    </div>
</template>
  
<script setup>
import { ref, onMounted } from 'vue';
import moment from 'moment';
import { FilterMatchMode } from 'primevue/api';

const products = ref([]);

const filters = ref();

// Define Filters
const initFilters = () => {
    filters.value = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    };
};
initFilters();

onMounted(async () => {
    try {
        // Get Data From Backend
        const response = await fetch('http://127.0.0.1:5000/');
        // Get JSON Object
        const fetchedData = await response.json();

        // Calculate person's age - Json date contains only person's birthday
        // Using Moment.js
        var today = moment()
        fetchedData.forEach(person => {
            let pDate = moment(person.birthdate)
            let diffyear = today.year() - pDate.year()
            person.age = diffyear;
        })

        products.value = fetchedData;
    } catch (error) {
        console.error('Fetch error:', error);
    }
});

</script>

<style>
.container {
    padding-left: 16px;
    padding-right: 16px;
}
</style>