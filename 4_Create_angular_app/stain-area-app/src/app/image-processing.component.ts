
// import { Component, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { Component, NgModule, NO_ERRORS_SCHEMA} from '@angular/core';
import { MessageService } from 'primeng/api';
import { FileUploadModule } from 'primeng/fileupload';
import { CommonModule } from '@angular/common';
import { TabViewModule } from 'primeng/tabview';
import { FormsModule } from '@angular/forms'; 
import { TableModule } from 'primeng/table';
import { SliderModule } from 'primeng/slider';
import { ButtonModule } from 'primeng/button';



@Component({
  selector: 'app-image-processing',
  templateUrl:'./image-processing.component.html',
  styleUrls: ['./image-processing.component.css'],
  providers: [MessageService],
  standalone: true, // Esto define que el componente es standalone
  
  imports: [CommonModule, FileUploadModule, TabViewModule,ButtonModule,  TableModule, FormsModule, SliderModule], // Importa los módulos necesarios aquí
})
export class ImageProcessingComponent {
  imageUrl: string = 'assets/Mancha.jpg';
  title = 'stain-area-app';
  image: any = null;
  n: number = 100; // Número de puntos aleatorios
  ni: number = 0; // Número de puntos dentro de la mancha
  estimatedArea: number = 0; // Área estimada
  previousResults: any[] = []; // Para almacenar los resultados anteriores

  // Función para cargar la imagen seleccionada
  onImageUpload(event: any) {
    const file = event.files[0];
    this.image = file;
    this.processImage(file);
  }

  // Lógica de procesamiento de la imagen
  processImage(file: File) {
    const imageUrl = URL.createObjectURL(file);
    const img = new Image();
    img.src = imageUrl;

    img.onload = () => {
      const canvas = document.createElement('canvas');
      const ctx = canvas.getContext('2d');
      if (ctx) {
        canvas.width = img.width;
        canvas.height = img.height;
        ctx.drawImage(img, 0, 0, img.width, img.height);
        const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
        const binaryImage = this.loadBinaryImage(imgData);
        this.calculateArea(binaryImage);
      }
    };
  }

  // Convertir la imagen a escala de grises y binarización
  loadBinaryImage(imgData: ImageData): number[][] {
    const binaryImage: number[][] = [];
    for (let y = 0; y < imgData.height; y++) {
      const row: number[] = [];
      for (let x = 0; x < imgData.width; x++) {
        const i = (y * imgData.width + x) * 4;
        const r = imgData.data[i];
        const g = imgData.data[i + 1];
        const b = imgData.data[i + 2];
        const gray = 0.3 * r + 0.59 * g + 0.11 * b;
        row.push(gray < 128 ? 1 : 0);
      }
      binaryImage.push(row);
    }
    return binaryImage;
  }

  // Generar puntos aleatorios
  generateRandomPoints(imageShape: [number, number], n: number): [number, number][] {
    const [height, width] = imageShape;
    const points: [number, number][] = [];
    for (let i = 0; i < n; i++) {
      const x = Math.floor(Math.random() * width);
      const y = Math.floor(Math.random() * height);
      points.push([x, y]);
    }
    return points;
  }

  // Contar cuántos puntos están dentro de la mancha
  countPointsInStain(points: [number, number][], binaryImage: number[][]): number {
    let ni = 0;
    points.forEach(([x, y]) => {
      if (binaryImage[y][x] === 1) {
        ni++;
      }
    });
    return ni;
  }

  // Estimar el área
  estimateArea(binaryImage: number[][], ni: number, n: number): number {
    const totalArea = binaryImage.length * binaryImage[0].length;
    return (totalArea * ni) / n;
  }

  // Función para calcular el área
  calculateArea(binaryImage: number[][]) {
    const randomPoints = this.generateRandomPoints(
      [binaryImage.length, binaryImage[0].length],
      this.n
    );
    this.ni = this.countPointsInStain(randomPoints, binaryImage);
    this.estimatedArea = this.estimateArea(binaryImage, this.ni, this.n);

    // Guardar el resultado
    this.previousResults.push({
      ni: this.ni,
      estimatedArea: this.estimatedArea,
      date: new Date(),
    });
  }
}

