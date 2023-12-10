import { createApp } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config';
import 'primevue/resources/themes/lara-light-green/theme.css'
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import InputText from 'primevue/inputtext'

const app = createApp(App);
app.use(PrimeVue);
app.component('Column', Column);
app.component('DataTable', DataTable);
app.component('InputText', InputText);
app.mount('#app');

